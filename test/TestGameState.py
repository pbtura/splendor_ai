'''
Created on Apr 12, 2023

@author: bucpa
'''
import unittest
import os
import csv
from ResourceCard import ResourceCard
from GameState import GameState
from Color import Color
from Cost import Cost
from NobleCard import NobleCard
from Player import Player
from TestGame import TestGame
from TokenStore import TokenStore


class TestGameState(TestGame):
    INITIAL_GEMS: dict = {Color.WHITE: 7, Color.BLUE: 7, Color.GREEN: 7, Color.RED: 7, Color.BLACK: 7, Color.GOLD: 5}

    game: GameState

    def setUp(self):
        self.game: GameState = GameState(os.path.join('..', 'resources', 'cards_list.csv'),
                                         os.path.join('..', 'resources', 'nobles_list.csv'))
        pass

    def tearDown(self):
        self.game = None
        pass

    def assertResourceCardsEqual(self, expected: ResourceCard, actual: ResourceCard):
        self.assertEqual(expected.level, actual.level)
        self.assertEqual(expected.points, actual.points)
        self.assertEqual(expected.suit, actual.suit)
        self.assertEqual(expected.cost, actual.cost)

    def assertNobleCardsEqual(self, expected: NobleCard, actual: NobleCard):
        self.assertEqual(expected.points, actual.points)
        self.assertEqual(expected.cost, actual.cost)

    def testImportResourceDecks(self):
        decks: dict = None
        with open(os.path.join('..', 'resources', 'cards_list.csv'), newline='') as f:
            reader = csv.DictReader(f)
            decks = GameState.importResourceDecks(reader)

        self.assertResourceDeckInitialized(decks)

        pass

    def testParseResourceRow(self):

        rowData: dict = {'Level': 1, 'Gem color': "BLUE", 'PV': 0, 'Price': "2g+2k", 'white': 0, 'blue': 0, 'green': 2,
                         'red': 0, 'black': 2}
        # (white, blue, green, red, black)
        expectedCost: Cost = Cost(0, 0, 2, 0, 2)
        expectedCard: ResourceCard = ResourceCard(1, Color.BLUE, expectedCost, 0)
        actualCard: ResourceCard = GameState.parseResourceRow(rowData)
        self.assertIsNotNone(actualCard)
        self.assertResourceCardsEqual(expectedCard, actualCard);
        pass

    def testInitializeResourceDeck(self):
        game: GameState = self.game
        game.initializeResourceDecks()

        self.assertResourceDeckInitialized(game.resourceDeck)
        pass

    def testInitializeAvailableGemsForTwoPlayers(self):

        game: GameState = self.game
        game.addPlayers(["a", "b"])
        game.initializeAvailableGems()

        self.assertAvailableGemsInitializedForTwoPlayers(game.availableGems)
        pass

    def testInitializeAvailableGemsForThreePlayers(self):

        game: GameState = self.game
        game.addPlayers(["a", "b", "c"])
        game.initializeAvailableGems()

        self.assertAvailableGemsInitializedForThreePlayers(game.availableGems)
        pass

    def testInitializeAvailableGemsForFourPlayers(self):

        game: GameState = self.game
        game.addPlayers(["a", "b", "c", "d"])
        game.initializeAvailableGems()

        self.assertAvailableGemsInitialized(game.availableGems)
        pass

    def testParseNobleRow(self):
        rowData: dict = {'PV': 3, 'white': 0, 'blue': 0, 'green': 4, 'red': 0, 'black': 4}
        expectedCost: Cost = Cost(0, 0, 4, 0, 4)
        expectedCard: NobleCard = NobleCard(expectedCost, 3)
        actualCard: NobleCard = GameState.parseNobleRow(rowData)
        self.assertIsNotNone(actualCard)
        self.assertNobleCardsEqual(expectedCard, actualCard);
        pass

    def testImportNobleDeck(self):
        decks: dict = None
        with open(os.path.join('..', 'resources', 'nobles_list.csv'), newline='') as f:
            reader = csv.DictReader(f)
            decks = GameState.importNobleDeck(reader)

        self.assertNobleDeckInitialized(decks)
        pass

    def testInitializeNobleDeck(self):
        game: GameState = self.game
        game.initializeNobleDeck()

        self.assertNobleDeckInitialized(game.noblesDeck)
        pass

    def testAddPlayers(self):
        game: GameState = self.game
        playerNames = ["playerA", "playerB"]
        game.addPlayers(playerNames)
        self.assertIsNotNone(game.players)
        self.assertEqual(2, len(game.players))

        player: Player
        for index, player in enumerate(game.players):
            self.assertEqual(playerNames[index], player.name)
        pass

    def testDealResourceCards(self):

        game: GameState = self.game
        game.initializeResourceDecks()
        deck1: list[ResourceCard] = game.resourceDeck.get(1)
        expected1: list[ResourceCard] = [deck1[0], deck1[1], deck1[2], deck1[3]]

        game.dealResourceCards(1, 4)
        # we want to test that the top 4 cards
        # have been moved to the availableResources deck
        self.assertEqual(36, len(game.resourceDeck.get(1)))
        actualDeck1: list = game.availableResources.get(1)
        self.assertEqual(4, len(actualDeck1))
        for idx, card in enumerate(actualDeck1):
            self.assertResourceCardsEqual(expected1[idx], card)

        pass

    def testDealNobleCards(self):
        game: GameState = self.game
        game.initializeNobleDeck()
        game.dealNobleCards(4)

        self.assertEqual(5, len(game.noblesDeck))
        self.assertEqual(5, len(game.availableNobles))
        pass

    def testDealNobleCardsForThreePlayers(self):
        game: GameState = self.game
        game.initializeNobleDeck()
        game.dealNobleCards(3)

        self.assertEqual(6, len(game.noblesDeck))
        self.assertEqual(4, len(game.availableNobles))
        pass

    def testDealNobleCardsForTwoPlayers(self):
        game: GameState = self.game
        game.initializeNobleDeck()
        game.dealNobleCards(2);

        self.assertEqual(7, len(game.noblesDeck))
        self.assertEqual(3, len(game.availableNobles))
        pass

    def testInitializeAvailableResourceCards(self):
        game: GameState = self.game
        game.initializeResourceDecks()
        deck1: list[ResourceCard] = game.resourceDeck.get(1)
        deck2: list[ResourceCard] = game.resourceDeck.get(2)
        deck3: list[ResourceCard] = game.resourceDeck.get(3)

        expected1: list[ResourceCard] = [deck1[0], deck1[1], deck1[2], deck1[3]]
        expected2: list[ResourceCard] = [deck2[0], deck2[1], deck2[2], deck2[3]]
        expected3: list[ResourceCard] = [deck3[0], deck3[1], deck3[2], deck3[3]]

        game.initializeAvailableResourceCards()

        actualDeck1: list = game.availableResources.get(1)
        actualDeck2: list = game.availableResources.get(2)
        actualDeck3: list = game.availableResources.get(3)
        self.assertAvailableResourcesDealt(game.resourceDeck, actualDeck1, actualDeck2, actualDeck3, False, expected1,
                                           expected2, expected3)

        pass

    def testSetupGame(self):
        names: list = ["playerA", "playerB", "playerC", "playerD"]
        game: GameState = self.game
        game.setupGame(names)

        # check players were initialized
        self.assertEqual(4, len(game.players))

        # check resource cards were initialized
        self.assertResourceDeckInitialized(game.resourceDeck)

        # check the nobles deck was initialized
        self.assertNobleDeckInitialized(game.noblesDeck)

        # check that the token bank was initialized
        self.assertAvailableGemsInitialized(game.availableGems)

        pass

    def testStartNewGame(self):

        names: list = ["playerA", "playerB", "playerC", "playerD"]
        game: GameState = self.game
        game.setupGame(names)

        game.startNewGame(1)

        # check randomize turn order
        self.assertTrue(game.playersRandomized)
        # check randomize resource deck
        self.assertTrue(game.resourcesShuffled)
        # check randomize noble deck
        self.assertTrue(game.noblesShuffled)

        # check deal resource cards
        actualDeck1: list = game.availableResources.get(1)
        actualDeck2: list = game.availableResources.get(2)
        actualDeck3: list = game.availableResources.get(3)
        self.assertAvailableResourcesDealt(game.resourceDeck, actualDeck1, actualDeck2, actualDeck3, 1)

        # check deal noble cards
        self.assertEqual(5, len(game.noblesDeck))
        self.assertEqual(5, len(game.availableNobles))

        pass

    def createGame(self) -> GameState:
        names: list = ["playerA", "playerB", "playerC", "playerD"]
        game: GameState = GameState(os.path.join('..', 'resources', 'cards_list.csv'),
                                    os.path.join('..', 'resources', 'nobles_list.csv'))
        game.setupGame(names)
        game.startNewGame(0)

        return game

    def testWithdrawGems(self):

        game: GameState = self.createGame()
        player: Player = game.players[0]

        # (white, blue, green, red, black)
        expectedCost: dict = {Color.WHITE: 0, Color.BLUE: 1, Color.RED: 1, Color.BLACK: 1}

        game.withdrawGems(player, expectedCost)
        actualPlayer = game.players[0]

        for x in expectedCost.keys():
            print(x)
            # check that the gems were withdrawn from the game store
            self.assertEqual(7 - expectedCost.get(x), game.availableGems.tokens.get(x))

            # check that the gems were added to the player store
            self.assertEqual(expectedCost.get(x), actualPlayer.gems.tokens.get(x))

        pass

    def testWithdrawGemPair(self):
        game: GameState = self.createGame()
        player: Player = game.players[0]

        # (white, blue, green, red, black)
        expectedCost: dict = {Color.BLUE: 2}

        game.withdrawGems(player, expectedCost)
        actualPlayer = game.players[0]

        for x in expectedCost.keys():
            # check that the gems were withdrawn from the game store
            self.assertEqual(5, game.availableGems.tokens.get(x))

            # check that the gems were added to the player store
            self.assertEqual(2, actualPlayer.gems.tokens.get(x))

    def testWithdrawTooManyGems(self):
        game: GameState = self.createGame()
        player: Player = game.players[0]

        # (white, blue, green, red, black)
        expectedCost: dict = {Color.WHITE: 1, Color.BLUE: 2}

        with self.assertRaises(RuntimeError) as context:
            game.withdrawGems(player, expectedCost)
        self.assertEqual(
            "Invalid withdraw. Valid combinations are 2 of a single color or one each of 3 different colors.",
            str(context.exception))

    def testWithdrawMoreGemsThanAvailable(self):
        game: GameState = self.createGame()
        player: Player = game.players[0]

        # (white, blue, green, red, black)
        expectedCost: dict = {Color.WHITE: 1}

        # withdraw gems until there are no white remaining
        i: int = 0
        while i < 7:
            game.withdrawGems(player, expectedCost)
            i += 1

        with self.assertRaises(RuntimeError) as context:
            game.withdrawGems(player, expectedCost)
        self.assertEqual("Cannot remove more gems than are in the store.", str(context.exception))

    def testWithdrawInvalidGemPair(self):
        game: GameState = self.createGame()
        player: Player = game.players[0]

        # withdraw gems until there are no white remaining
        i: int = 0
        while i < 4:
            game.withdrawGems(player, {Color.WHITE: 1})
            i += 1

        with self.assertRaises(RuntimeError) as context:
            game.withdrawGems(player, {Color.WHITE: 2})
        self.assertEqual("Cannot withdraw two matched gems when less than four remain.", str(context.exception))

    def testPurchaseCard(self):

        game: GameState = self.createGame()
        player: Player = game.players[0]
        # setup the player with enough gems for the purchase
        game.withdrawGems(player, {Color.WHITE: 1, Color.BLUE: 1, Color.GREEN: 1})
        game.withdrawGems(player, {Color.WHITE: 1, Color.RED: 1, Color.BLACK: 1})

        deckKey: int = 1
        cardIdx: int = 0

        # Level    Gem color    PV    (w)hite    bl(u)e    (g)reen    (r)ed    blac(k)
        #    1    BLACK        0     1          1         1          1        0                                                                
        expected: ResourceCard = game.availableResources.get(deckKey)[cardIdx]
        expectedReplacement: ResourceCard = game.resourceDeck.get(deckKey)[0]
        gems: dict = {Color.WHITE: expected.cost.white, Color.BLUE: expected.cost.blue,
                      Color.GREEN: expected.cost.green, Color.RED: expected.cost.red, Color.BLACK: expected.cost.black,
                      Color.GOLD: 0}

        game.purchaseCard(player, deckKey, expected, gems)
        actualPlayer: Player = game.players[0]

        # check that the card was transferred to the player
        self.assertEqual(1, len(actualPlayer.cards))
        self.assertResourceCardsEqual(expected, actualPlayer.cards[0])

        # check that the correct amount of gems were transfered from
        # the player to the bank
        self.assertDictEqual(
            {Color.WHITE: 1, Color.BLUE: 0, Color.GREEN: 0, Color.RED: 0, Color.BLACK: 1, Color.GOLD: 0},
            player.gems.tokens)
        self.assertDictEqual(
            {Color.WHITE: 6, Color.BLUE: 7, Color.GREEN: 7, Color.RED: 7, Color.BLACK: 6, Color.GOLD: 5},
            game.availableGems.tokens)

        # make sure the purchased card was replaced
        self.assertEqual(4, len(game.availableResources.get(deckKey)))
        self.assertEqual(35, len(game.resourceDeck.get(deckKey)))
        self.assertIn(expectedReplacement, game.availableResources.get(deckKey))

        pass

    def testWithdrawPlayerGems(self):
        game: GameState = self.createGame()
        player: Player = game.players[0]
        # setup the player with enough gems for the purchase
        game.withdrawGems(player, {Color.WHITE: 1, Color.BLUE: 1, Color.GREEN: 1})
        game.withdrawGems(player, {Color.WHITE: 1, Color.RED: 1, Color.BLACK: 1})

        player.gems.withdrawTokens({Color.WHITE: 2})
        self.assertDictEqual(
            {Color.WHITE: 0, Color.BLUE: 1, Color.GREEN: 1, Color.RED: 1, Color.BLACK: 1, Color.GOLD: 0},
            player.gems.tokens)
        pass

    def testPurchaseCardUsingGold(self):

        game: GameState = self.createGame()
        player: Player = game.players[0]
        # setup the player with enough gems for the purchase
        game.withdrawGems(player, {Color.WHITE: 1, Color.BLUE: 1, Color.GREEN: 1})
        game.withdrawGems(player, {Color.WHITE: 1, Color.RED: 1, Color.GOLD: 1})

        deckKey: int = 1
        cardIdx: int = 0

        # Level    Gem color    PV    (w)hite    bl(u)e    (g)reen    (r)ed    blac(k)
        #    1    BLACK        0     1          1         1          1        0                                                                
        expected: ResourceCard = game.availableResources.get(deckKey)[cardIdx]
        expectedReplacement: ResourceCard = game.resourceDeck.get(deckKey)[0]
        gems: TokenStore = {Color.WHITE: 0, Color.BLUE: expected.cost.blue, Color.GREEN: expected.cost.green,
                            Color.RED: expected.cost.red, Color.BLACK: expected.cost.black, Color.GOLD: 1}

        game.purchaseCard(player, deckKey, expected, gems)
        actualPlayer: Player = game.players[0]

        # check that the card was transferred to the player
        self.assertEqual(1, len(actualPlayer.cards))
        self.assertResourceCardsEqual(expected, actualPlayer.cards[0])

        # check that the correct amount of gems were transfered from
        # the player to the bank
        self.assertDictEqual(
            {Color.WHITE: 2, Color.BLUE: 0, Color.GREEN: 0, Color.RED: 0, Color.BLACK: 0, Color.GOLD: 0},
            player.gems.tokens)
        self.assertDictEqual(
            {Color.WHITE: 5, Color.BLUE: 7, Color.GREEN: 7, Color.RED: 7, Color.BLACK: 7, Color.GOLD: 5},
            game.availableGems.tokens)

        # make sure the purchased card was replaced
        self.assertEqual(4, len(game.availableResources.get(deckKey)))
        self.assertEqual(35, len(game.resourceDeck.get(deckKey)))
        self.assertIn(expectedReplacement, game.availableResources.get(deckKey))

        pass

    def testPurchaseCardWithInsufficientGems(self):

        game: GameState = self.createGame()
        player: Player = game.players[0]
        # setup the player such that they don't have the required (red) gems for the purchase
        game.withdrawGems(player, {Color.WHITE: 1, Color.BLUE: 1, Color.GREEN: 1})

        deckKey: int = 1
        cardIdx: int = 0

        # Level    Gem color    PV    (w)hite    bl(u)e    (g)reen    (r)ed    blac(k)
        #    1    BLACK        0     1          1         1          1        0                                                                
        expected: ResourceCard = game.availableResources.get(deckKey)[cardIdx]
        gems: dict = {Color.WHITE: expected.cost.white, Color.BLUE: expected.cost.blue,
                      Color.GREEN: expected.cost.green, Color.RED: expected.cost.red, Color.BLACK: expected.cost.black,
                      Color.GOLD: 0}

        with self.assertRaises(RuntimeError) as context:
            game.purchaseCard(player, deckKey, expected, gems)
        self.assertEqual("Cannot remove more gems than are in the store.", str(context.exception))
        pass

    def testReserveCard(self):

        game: GameState = self.createGame()
        player: Player = game.players[0]
        deckKey: int = 1
        cardIdx: int = 0

        # Level    Gem color    PV    (w)hite    bl(u)e    (g)reen    (r)ed    blac(k)
        #    1    BLACK        0     1          1         1          1        0                                                                
        expected: ResourceCard = game.availableResources.get(deckKey)[cardIdx]

        expectedReplacement: ResourceCard = game.resourceDeck.get(deckKey)[0]

        game.reserveCard(player, deckKey, expected)

        # check that a gold token was transferred from the bank to the player
        self.assertDictEqual(
            {Color.WHITE: 0, Color.BLUE: 0, Color.GREEN: 0, Color.RED: 0, Color.BLACK: 0, Color.GOLD: 1},
            player.gems.tokens)
        self.assertDictEqual(
            {Color.WHITE: 7, Color.BLUE: 7, Color.GREEN: 7, Color.RED: 7, Color.BLACK: 7, Color.GOLD: 4},
            game.availableGems.tokens)

        # check that the card was transferred to the player
        self.assertResourceCardsEqual(expected, player.reservedCards[0])

        # make sure the reserved card was replaced
        self.assertEqual(4, len(game.availableResources.get(deckKey)))
        self.assertEqual(35, len(game.resourceDeck.get(deckKey)))

        self.assertIn(expectedReplacement, game.availableResources.get(deckKey))
        pass

    def testReserveTooManyCards(self):

        game: GameState = self.createGame()
        player: Player = game.players[0]
        deckKey: int = 1
        cardIdx: int = 0
        expected: ResourceCard = game.availableResources.get(deckKey)[cardIdx]

        game.reserveCard(player, deckKey, expected)

        expected: ResourceCard = game.availableResources.get(deckKey)[cardIdx]
        game.reserveCard(player, deckKey, expected)

        expected: ResourceCard = game.availableResources.get(deckKey)[cardIdx]
        game.reserveCard(player, deckKey, expected)

        with self.assertRaises(RuntimeError) as context:
            expected: ResourceCard = game.availableResources.get(deckKey)[cardIdx]
            game.reserveCard(player, deckKey, expected)
        self.assertEqual("A player cannot reserve more than three cards at once.", str(context.exception))

    def testClaimReservedCard(self):

        game: GameState = self.createGame()
        player: Player = game.players[0]
        deckKey: int = 1
        cardIdx: int = 0

        # Level    Gem color    PV    (w)hite    bl(u)e    (g)reen    (r)ed    blac(k)
        #    1    BLACK        0     1          1         1          1        0                                                                
        expected: ResourceCard = game.availableResources.get(deckKey)[cardIdx]
        gems: dict = {Color.WHITE: expected.cost.white, Color.BLUE: expected.cost.blue,
                      Color.GREEN: expected.cost.green, Color.RED: expected.cost.red, Color.BLACK: expected.cost.black,
                      Color.GOLD: 0}

        # setup the player with enough gems for the purchase
        game.withdrawGems(player, {Color.WHITE: 1, Color.BLUE: 1, Color.GREEN: 1})
        game.withdrawGems(player, {Color.WHITE: 1, Color.RED: 1, Color.BLACK: 1})

        # reserve the card
        game.reserveCard(player, deckKey, expected)

        # claim the reserved card
        game.claimReservedCard(player, expected, gems)

        # check that the correct amount of gems were transfered from the player to the bank
        self.assertDictEqual(
            {Color.WHITE: 1, Color.BLUE: 0, Color.GREEN: 0, Color.RED: 0, Color.BLACK: 1, Color.GOLD: 1},
            player.gems.tokens)
        self.assertDictEqual(
            {Color.WHITE: 6, Color.BLUE: 7, Color.GREEN: 7, Color.RED: 7, Color.BLACK: 6, Color.GOLD: 4},
            game.availableGems.tokens)

        # check that the card was moved from the reserved list to the players cards
        self.assertEqual(0, len(player.reservedCards))
        self.assertResourceCardsEqual(expected, player.cards[0])
        pass

    def testClaimNoble(self):

        game: GameState = self.createGame()
        player: Player = game.players[0]
        cardIdx: int = 0

        # PV    white    blue    green    red    black
        # 3    0        0       4        4      0
        expected: NobleCard = game.availableNobles[0]

        idx: int = 21
        while idx < 25:
            card1: ResourceCard = game.resourceDeck.get(1)[idx]
            player.cards.append(card1)
            idx += 1

        idx: int = 29
        while idx < 33:
            card2: ResourceCard = game.resourceDeck.get(1)[idx]
            player.cards.append(card2)
            idx += 1

        game.claimNoble(player, expected)

        self.assertEqual(4, len(game.availableNobles))
        self.assertEqual(1, len(player.nobles))
        self.assertNobleCardsEqual(expected, player.nobles[0])

        pass

    def testClaimInvalidNoble(self):

        game: GameState = self.createGame()
        player: Player = game.players[0]
        expected: NobleCard = game.availableNobles[0]

        card1: ResourceCard = game.resourceDeck.get(3)[9]

        player.cards.append(card1)

        # PV    white    blue    green    red    black
        # 3    0        0       4        4      0       

        with self.assertRaises(RuntimeError) as context:
            game.claimNoble(player, expected)
        self.assertEqual("Not enough resource cards to claim a noble.", str(context.exception))

    def testIsCardAffordable(self):
        game: GameState = self.createGame()
        player: Player = game.players[0]

        deckKey: int = 1
        cardIdx: int = 0

        expected: ResourceCard = game.availableResources.get(deckKey)[cardIdx]
        # setup the player with enough gems for the purchase
        game.withdrawGems(player, {Color.WHITE: 1, Color.BLUE: 1, Color.GREEN: 1})
        game.withdrawGems(player, {Color.WHITE: 1, Color.RED: 1, Color.GREEN: 1})

        # reserve a card to add a gold gem
        game.reserveCard(player, deckKey, expected)

        # test a card affordable without gold
        # Level    Gem color    PV    (w)hite    bl(u)e    (g)reen    (r)ed    blac(k)
        #    1    BLACK        0     0          0         2          1        0    
        card: ResourceCard = game.availableResources.get(1)[3]
        # print(card)

        self.assertTrue(GameState.canPurchase(card.cost, player.gems, list(player.getResourceTotals().values())))

    def testIsCardNotAffordable(self):
        game: GameState = self.createGame()
        player: Player = game.players[0]

        deckKey: int = 1
        cardIdx: int = 0
        expected: ResourceCard = game.availableResources.get(deckKey)[cardIdx]

        # setup the player with enough gems for the purchase
        game.withdrawGems(player, {Color.WHITE: 1, Color.BLUE: 1, Color.GREEN: 1})
        game.withdrawGems(player, {Color.WHITE: 1, Color.RED: 1, Color.GREEN: 1})

        # reserve a card to add a gold gem
        game.reserveCard(player, deckKey, expected)

        # test a card that is not affordable
        # Level    Gem color    PV    (w)hite    bl(u)e    (g)reen    (r)ed    blac(k)
        #    1    BLACK        0     0          0         1          3        1    
        card: ResourceCard = game.availableResources.get(1)[2]
        # print(card)

        self.assertFalse(GameState.canPurchase(card.cost, player.gems, list(player.getResourceTotals().values())))

        pass

    def testIsCardAffordableWithGold(self):
        game: GameState = self.createGame()
        player: Player = game.players[0]

        deckKey: int = 1
        cardIdx: int = 0
        expected: ResourceCard = game.availableResources.get(deckKey)[cardIdx]

        # setup the player enough gems for the purchase
        game.withdrawGems(player, {Color.WHITE: 1, Color.BLUE: 1, Color.GREEN: 1})
        game.withdrawGems(player, {Color.WHITE: 1, Color.RED: 1, Color.GREEN: 1})

        # reserve a card to add a gold gem
        game.reserveCard(player, deckKey, expected)

        # test a card affordable if gold is used
        # Level    Gem color    PV    (w)hite    bl(u)e    (g)reen    (r)ed    blac(k)
        #    1    BLACK        0     2          2         0          1        0    
        card: ResourceCard = game.availableResources.get(1)[1]
        # print(card)

        self.assertTrue(GameState.canPurchase(card.cost, player.gems, list(player.getResourceTotals().values())))

        pass

    def testIsCardAffordableWithDiscounts(self):
        game: GameState = self.createGame()
        player: Player = game.players[0]

        # add enough cards to the player to reduce the cost of the card being
        # purchased to an affordable state
        crd1: ResourceCard = ResourceCard(1, Color.RED, Cost(3, 0, 0, 0, 0), 0)
        crd2: ResourceCard = ResourceCard(1, Color.BLACK, Cost(0, 0, 3, 0, 0), 0)
        player.cards.append(crd1)
        player.cards.append(crd2)

        # setup the player with gems for the purchase
        game.withdrawGems(player, {Color.WHITE: 1, Color.RED: 1, Color.GREEN: 1})
        game.withdrawGems(player, {Color.WHITE: 1, Color.RED: 1, Color.GREEN: 1})

        # test a card that is not affordable
        # Level    Gem color    PV    (w)hite    bl(u)e    (g)reen    (r)ed    blac(k)
        #    1    BLACK        0     0          0         1          3        1    
        card: ResourceCard = game.availableResources.get(1)[3]
        cardId: str = "1BLACK[00131]"
        self.assertEqual(cardId, card.id)
        # print(card)
        discounts = player.getResourceTotals().values()
        self.assertTrue(GameState.canPurchase(card.cost, player.gems, list(discounts)))

        pass

    def testFilterAffordableCards(self):

        game: GameState = self.createGame()
        player: Player = game.players[0]

        deckKey: int = 1
        cardIdx: int = 0
        expected: ResourceCard = game.availableResources.get(deckKey)[cardIdx]

        # setup the player with enough gems for the purchase
        game.withdrawGems(player, {Color.WHITE: 1, Color.BLUE: 1, Color.GREEN: 1})
        game.withdrawGems(player, {Color.WHITE: 1, Color.RED: 1, Color.GREEN: 1})

        # reserve a card to add a gold gem
        game.reserveCard(player, deckKey, expected)

        results: [ResourceCard] = GameState.findAvailableResources(player.gems, game.availableResources,
                                                                   list(player.getResourceTotals().values()))
        print(results)
        self.assertEqual(3, len(results))

        pass

    def testFilterAffordableCardsWithDiscounts(self):

        game: GameState = self.createGame()
        player: Player = game.players[0]

        # setup the player with enough gems for the purchase
        player.gems = TokenStore(2, 1, 0, 1, 2, 1)

        # add enough cards to the player to reduce the cost of the card being
        # purchased to an affordable state
        crd1: ResourceCard = ResourceCard(1, Color.RED, Cost(3, 0, 0, 0, 0), 0)
        crd2: ResourceCard = ResourceCard(1, Color.BLUE, Cost(0, 0, 3, 0, 0), 0)
        player.cards.append(crd1)
        player.cards.append(crd2)

        results: [ResourceCard] = GameState.findAvailableResources(player.gems, game.availableResources,
                                                                   list(player.getResourceTotals().values()))
        print(f"affordable {results}")
        self.assertEqual(3, len(results))

        pass


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testParseResourceRow']
    unittest.main()
