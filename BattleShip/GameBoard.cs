using System;

namespace BattleShip
{
    public class Cordinates
    {
        public int Row { get; set; }
        public int Column { get; set;}

        public Cordinates(int row, int column)
        {
            Row=row;
            Column=column;
        }
    }
    public enum OccupationType
    {
        [Description("o")]
        Empty,

        [Description("B")]
        Battleship,

        [Description("C")]
        Cruiser,

        [Description("D")]
        Destroyer,

        [Description("S")]
        Submarine,

        [Description("A")]
        Carrier,

        [Description("X")]
        Hit,

        [Description("M")]
        Miss
    }

    public class Panel
    {
        public OccupationType OccupationType { get; set; }
        public Cordinates Cordinates { get; set; }

        public Panel(int row, int column)
        {
            Crodinated = new Cordinates(row, column);
            OccupationType = OccupationType.Empty;

        }
        
        public string status
        {
            get
            {
                return OccupationType.GetAttributeOfType<DescriptionType>().Description;
            }
            
        }
        public bool isOccupied
        {
            get
            {
                
            }
            
        }
    }
}