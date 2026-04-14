using System;

namespace EjerciciosLogica
{
    class Programa
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== EJERCICIO 9: NÚMEROS PARES ===");
            ImprimirNumerosPares();
            
            Console.WriteLine("\n----------------------------------\n");
            
            Console.WriteLine("\nPresiona cualquier tecla para salir...");
            Console.ReadKey();
        }

        static void ImprimirNumerosPares(){
            for (int i = 1; i <= 50; i++)
            {

                if (i % 2 == 0)
                {
                    Console.WriteLine($"Número par encontrado: {i}");
                }
            }
         }
    }
}