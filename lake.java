/* Copyright 2009-2016 David Hadka
 *
 * This file is part of the MOEA Framework.
 *
 * The MOEA Framework is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or (at your
 * option) any later version.
 *
 * The MOEA Framework is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
 * or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public
 * License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with the MOEA Framework.  If not, see <http://www.gnu.org/licenses/>.
 */
import java.io.File;
import java.io.IOException;

import org.moeaframework.Executor;
import org.moeaframework.core.NondominatedPopulation;
import org.moeaframework.core.Solution;
import org.moeaframework.core.variable.RealVariable;
import org.moeaframework.problem.ExternalProblem;

/**
 * Demonstrates how problems can be defined externally to the MOEA Framework,
 * possibly written in a different programming language.  In this case, the
 * problem is defined in the file ./examples/dtlz2.c using the C programming
 * language.  Run the command 'make' in the ./examples/ folder to compile
 * the executable.
 */


	/**
	 * The ExternalProblem opens a communication channel with the external
	 * process defined in the constructor.
	 */
public class lake extends ExternalProblem {

		public lake() throws IOException {
			super("./lake");
		}

		@Override
		public String getName() {
			return "lake";
		}

		@Override
		public int getNumberOfVariables() {
			return 6;
		}

		@Override
		public int getNumberOfObjectives() {
			return 4;
		}

		@Override
		public int getNumberOfConstraints() {
			return 1;
		}

		@Override
		public Solution newSolution() {
			Solution solution = new Solution(getNumberOfVariables(), 
					getNumberOfObjectives(),getNumberOfConstraints());

			for (int i = 0; i < getNumberOfVariables(); i++) {
				solution.setVariable(i, new RealVariable(0.0, 1.0));
			}

			return solution;
		}
		
	}

